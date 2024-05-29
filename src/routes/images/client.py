import os
import base64

from imagekitio import ImageKit
from imagekitio.models.results import UploadFileResult
from fastapi import UploadFile, HTTPException
from src.routes.images.models import Image

class ImageKitClient:
    def __init__(self):
        self.client = ImageKit(
            public_key=os.getenv("IMAGE_KIT_PUBLIC_KEY"),
            private_key=os.getenv("IMAGE_KIT_PRIVATE_KEY"),
            url_endpoint=os.getenv("IMAGE_KIT_ENDPOINT")
        )

    async def upload(self, file: UploadFile):
        try:
            file_content = await file.read()

            if not file_content:
                raise HTTPException(status_code=400, detail="File content is empty")

            upload_response = self.client.upload(
                file=base64.b64encode(file_content),
                file_name=file.filename
            )

            return self.convert_to_image(upload_response)
        except HTTPException as e:
            raise e
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")
        
    def delete_by_id(self, id: str):
        try:
            self.client.delete_file(file_id=id)
        except HTTPException as e:
            raise e
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")
    
    def convert_to_image(self, upload_response: UploadFileResult):
        image = Image()
        image.id = upload_response.file_id
        image.url = upload_response.url
        return image