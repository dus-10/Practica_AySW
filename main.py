from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Lista temporal para guardar reservas (simula base de datos)
reservas = []

class Reserva(BaseModel):
    id_reserva: int
    id_sala: int
    id_usuario: int
    fecha: str
    hora_inicio: str
    hora_fin: str
    personas: int
    estado: str


@app.post("/reservas")
async def crear_reserva(reserva: Reserva):
    reservas.append(reserva)
    return {"mensaje": "Reserva creada correctamente", "reserva": reserva}


    # GET - Listar reservas
@app.get("/reservas", response_model=List[Reserva])
async def listar_reservas():
    return reservas
