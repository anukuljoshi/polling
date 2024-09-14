from fastapi import BackgroundTasks, FastAPI

app = FastAPI()


def write_notification(email: str, message: str = ""):
    """write notification details to log file"""
    with open("log.txt", "w+", encoding="utf-8") as log_file:
        content = f"notification for {email}: {message}"
        log_file.write(content)


@app.post("/send-notification/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    """handler to send a notification in background tasks"""
    background_tasks.add_task(
        write_notification, email, message="some notification"
    )
    return {"message": "Notification sent in the background."}
