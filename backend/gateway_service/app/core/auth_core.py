from fastapi import HTTPException, status
from app.core.config import settings
import requests


def user_login(request):
    auth = request.authorization
    if not auth:
        return HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Not authenticated"
        )
    basicAuth = (auth.username, auth.password)
    response = requests.post(
        url=f"{settings.AUTH_SERVICE_BASEURL}/login",
        auth=basicAuth,
    )

    if response.status_code == 200:
        return response.text

    else:
        return response.text
