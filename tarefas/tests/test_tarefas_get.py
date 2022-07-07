from django.urls import reverse
from pytest_django.asserts import assertContains
import pytest
from tarefas.models import Tarefa


@pytest.fixture
def resposta(client, db):
    resp = client.get(reverse('tarefas:index'))
    return resp

def test_status_code(resposta):
    assert resposta.status_code == 200

def test_se_o_formulario_esta_presente(resposta):
    assertContains(resposta, '<form')

def test_se_o_botao_salvar_e_do_tipo_submit(resposta):
    assertContains(resposta, '<button type="submit"')


@pytest.fixture
def lista_de_tarefas_pendentes(db):
    tarefas = [
        Tarefa(nome='Tarefa 1', feita=False),
        Tarefa(nome='Tarefa 2', feita=False),
    ]
    Tarefa.objects.bulk_create(tarefas)
    return tarefas


@pytest.fixture
def resposta_com_lista_de_tarefas(client, lista_de_tarefas_pendentes):
    resp = client.get(reverse('tarefas:index'))
    return resp


def test_se_lista_de_tarefas_pendentes_presente_no_html(resposta_com_lista_de_tarefas, lista_de_tarefas_pendentes):
    for tarefa in lista_de_tarefas_pendentes:
        assertContains(resposta_com_lista_de_tarefas, tarefa.nome)