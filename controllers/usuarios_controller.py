from fastapi import APIRouter, Response, status
import ormar
from models.usuario_model import Usuario, metadata, database
from models.usuario_update import UsuarioUpdate
import psycopg2

router = APIRouter()



#Post Usuario

@router.post("/",
            summary='Cria um novo usuário',
            description='CRUD FastAPI Ormar SQLite - CREATE ',tags=['usuarios'])
async def post_usuario(usuario: Usuario):
    
    usuario.id = 0
    await usuario.save()
    return usuario


# Get Usuarios 

@router.get('/',
            summary='Lista todos os usuários', 
            description='CRUD FastAPI Ormar SQLite - READ', tags=['usuarios'])
async def get_usuarios():
    return await Usuario.objects.all()


#Get Usuario por ID 

@router.get('/{usuario_id}',
            summary='Lista um usuário', 
            description='CRUD - FastAPI Ormar SQLite - READ ', tags=['usuarios'])
async def get_usuarios_por_id(usuario_id : int , response: Response):
    try:
        usuario = await Usuario.objects.get(id=usuario_id)
        return usuario
    except ormar.exceptions.NoMatch:
        response.status_code = 404
        return {'Mensagem': f'Usuário com ID {usuario_id} nāo encontrado.'}


#Patch usuario - update parcial (email e telefone)
    
@router.patch('/{usuario_id}', 
            summary='Atualiza parcialmente usuário', 
            description='CRUD - FastAPI Ormar SQLite - UPDATE ', tags=['usuarios'])
async def patch_usuario(propriedades_atualizacao: UsuarioUpdate, usuario_id: int, response: Response):
    try:
        usuario_salvo = await Usuario.objects.get(id=usuario_id)
        propriedades_atualizadas = propriedades_atualizacao.dict(exclude_unset=True)
        await usuario_salvo.update(**propriedades_atualizadas)
        return usuario_salvo
    except ormar.exceptions.NoMatch:
        response.status_code = 404
        return {'Mensagem': f'Usuário com ID {usuario_id} nāo encontrado.'}


#Put usuario - update total         

@router.put('/{usuario_id}',
            summary='Atualiza usuário', 
            description='CRUD - FastAPI Ormar SQLite - UPDATE ', tags=['usuarios'])
async def put_usuario(usuario_id: int, usuario: Usuario, response: Response):
    try:
        usuario_db = await Usuario.objects.get(id=usuario_id)
        usuario.id = usuario_db.id
        return await usuario_db.update(**usuario.dict())

    except ormar.exceptions.NoMatch:
        response.status_code = 404
        return {'Mensagem': f'Usuário com ID {usuario_id} nāo encontrado.'}


#Deleta usuario         

@router.delete('/{usuario_id}',
            summary='Deleta um usuário', 
            description='CRUD - FastAPI Ormar SQLite - DELETE ', tags=['usuarios'])
async def delete_usuario(usuario_id: int, response: Response):
    try:
        usuario = await Usuario.objects.get(id=usuario_id)
        return await usuario.delete()
    except ormar.exceptions.NoMatch:
        response.status_code = 404
        return {'Mensagem': f'Usuário com ID {usuario_id} nāo encontrado.'}