from bentoml import env, artifacts, api, BentoService
from bentoml.adapters import JsonInput
from bentoml.service.artifacts.common import TextFileArtifact
from sinara.bentoml_artifacts.binary_artifact import BinaryFileArtifact

@env()

@artifacts([
    BinaryFileArtifact('ml_model_version')
])
class SimplePytorchLightning(BentoService):
    """
    Здесь будет описание
    """

    @api(input=JsonInput())
    def ml_model_version(self, *args):
        """
        Run ID компонента, создавшего данную версию сервиса.
        """
        return self.artifacts.ml_model_version

    @api(input=JsonInput())
    def service_version(self, *args):
        """
        Версия данного Bento сервиса.
        """
        return self.version
    