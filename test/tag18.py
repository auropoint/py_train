# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture. destroy)
    return fixture


def test_tab(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="g", header="gh", footer="gf"))
    app.session.logout()


def test_tab_empty(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()

