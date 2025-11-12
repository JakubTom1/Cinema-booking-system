from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from backend.database import init_db
from backend.routes import auth, movies, showings, reservations, admin, programme, delete_ticket
from backend.routes.auth import get_current_user
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:63342", "http://127.0.0.1:5500", "http://127.0.0.2:5501","http://127.0.0.1:8000 "],  # Zezwól na dostęp z tego portu
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_db()

app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(movies.router, prefix="/movies", tags=["Movies"])
app.include_router(showings.router, prefix="/showings", tags=["Showings"])
app.include_router(reservations.router, prefix="/reservations", tags=["Reservations"], dependencies=[Depends(get_current_user)])
#app.include_router(admin.router, prefix="/admin", tags=["Admin"], dependencies=[Depends(get_current_user)])
#app.include_router(reports.router, prefix="/reports", tags=["Reports"])

app.include_router(programme.router, prefix = "", tags=["Programme"])
#app.include_router(delete_ticket.router, prefix = "", tags = ["Delete Ticket"], dependencies=[Depends(get_current_user)])


@app.get("/", status_code=status.HTTP_200_OK)
def root():
    return {"message": "Cinema booking API is running."}