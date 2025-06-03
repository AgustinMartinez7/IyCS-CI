from locust import HttpUser, task

class UsuarioSimulado(HttpUser):
    @task
    def test_doble(self):
        self.client.get("/doble?numero=5")

