# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture. destroy)
    return fixture


def test_tab(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="g", header="gh", footer="gf"))
    app.logout()


def test_tab_empty(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()

