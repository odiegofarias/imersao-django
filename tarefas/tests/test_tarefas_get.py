from django.urls import reverse
from django.test import Client
from pytest_django.asserts import assertContains
import pytest

@pytest.fixture
def resposta(client):
    resp = client.get(reverse('tarefas:index'))
    return resp

def test_status_code(resposta):
    assert resposta.status_code == 200

def test_se_o_formulario_esta_presente(resposta):
    assertContains(resposta, '<form')

def test_se_o_botao_salvar_e_do_tipo_submit(resposta):
    assertContains(resposta, '<button type="submit"')

