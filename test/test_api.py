"""API 测试"""

import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root():
    """测试根路径"""
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_health():
    """测试健康检查"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_open_api_health():
    """测试 Open API 健康检查"""
    response = client.get("/api/open/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_internal_api_health():
    """测试 Internal API 健康检查"""
    response = client.get("/api/internal/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


