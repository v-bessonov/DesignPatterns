import uuid


class ApplicationState:
    instance = None

    def __init__(self):
        self.id = uuid.uuid4()

    @staticmethod
    def get_app_state():
        if not ApplicationState.instance:
            ApplicationState.instance = ApplicationState()
        return ApplicationState.instance

    def __str__(self):
        return f'id: {self.id}'
