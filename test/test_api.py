from app.api import app

def test_reserva_exitosa():
    cliente = app.test_client()
    resp = cliente.post('/reservar', json={"sala": "B", "hora": "14:00"})
    assert resp.status_code == 201

def test_reserva_duplicada():
    cliente = app.test_client()
    # Primera reserva
    cliente.post('/reservar', json={"sala": "B", "hora": "14:00"})
    # Segunda reserva (duplicada)
    resp = cliente.post('/reservar', json={"sala": "B", "hora": "14:00"})
    assert resp.status_code == 409