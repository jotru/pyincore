import pytest

from pyincore import IncoreClient, InsecureIncoreClient
from pyincore import HazardService


@pytest.fixture
def hazardsvc():
    cred = None
    try:
        with open(".incorepw", 'r') as f:
            cred = f.read().splitlines()
    except EnvironmentError:
        return None
    #client = IncoreClient("https://incore2-services.ncsa.illinois.edu", cred[0], cred[1])
    client =   InsecureIncoreClient("http://incore2-services.ncsa.illinois.edu:8888",
            cred[0])

    return HazardService(client)


def test_get_earthquake_hazard_value(hazardsvc):
    """
    testing getting hazard value
    https://incore2-services.ncsa.illinois.edu/hazard/api/earthquakes/59f3315ec7d30d4d6741b0bb/value?demandType=0.2+SA&demandUnits=g&siteLat=35.07899&siteLong=-90.0178
    """
    if hazardsvc is None:
        assert False, ".incorepw does not exist!"
    hval = hazardsvc.get_earthquake_hazard_value("5b902cb273c3371e1236b36b", "0.2 SA", "g", 35.07899, -90.0178)
    assert hval == 0.5322993805448739


def test_get_earthquake_hazard_values(hazardsvc):
    """
    Testing getting multiple hazard values
    """
    if hazardsvc is None:
        assert False, ".incorepw does not exist!"
    hvals = hazardsvc.get_earthquake_hazard_values("5b902cb273c3371e1236b36b", "0.2 SA", "g",
                                                   [35.07899, -90.0178, 35.17899, -90.0178])
    assert hvals[0]['hazardValue'] == 0.5322993805448739 and hvals[1]['hazardValue'] == 0.5926201634382787

#TODO: This geologydataset is only available on gowtham's local. Test with a real dataset once nebula is back
def test_get_liquefaction_values(hazardsvc):
    if hazardsvc is None:
        assert False, ".incorepw does not exist!"
    liq_vals = hazardsvc.get_liquefaction_values("59f3315ec7d30d4d6741b0bb","5ad506f5ec23094e887f4760", "in",
                                ["35.07899,-90.0178", "35.17899,-90.0178"])
    assert liq_vals[0]['pgd'] == 23.21177309712353 and liq_vals[1]['pgd'] == 97.25585469955409

def test_create_earthquake(hazardsvc):
    """
    Test creating earthquake
    """
    if hazardsvc is None:
        assert False, ".incorepw does not exist!"
    config = ""
    with open("eq.json", 'r') as file:
        config = file.read()
    response = hazardsvc.create_earthquake(config)
    assert response["id"] is not None


def test_create_tornado_scenario(hazardsvc):
    if hazardsvc is None:
        assert False, ".incorepw does not exist!"

    scenario = ""
    with open("tornado.json", 'r') as file:
        scenario = file.read()

    response = hazardsvc.create_tornado_scenario(scenario)
    assert response["id"] is not None


def test_get_tornado_hazard_value(hazardsvc):
    if hazardsvc is None:
        assert False, ".incorepw does not exist!"

    hval = hazardsvc.get_tornado_hazard_value("5ad0f35eec230965e6d98d0c", "mph", 35.228, -97.478, 0)
    assert ((hval > 85) and (hval <  165))


def test_get_tornado_hazard_values(hazardsvc):
    """
    Testing getting multiple hazard values
    """
    if hazardsvc is None:
        assert False, ".incorepw does not exist!"
    hvals = hazardsvc.get_tornado_hazard_values("5ad0f35eec230965e6d98d0c", "mph",
                                                   [35.228, -97.478, 35.229, -97.465])

    assert ((hvals[0]['hazardValue'] > 85) and (hvals[0]['hazardValue'] < 165)) and hvals[1]['hazardValue'] == 0

def test_create_hurricane_windfield(hazardsvc):
    if hazardsvc is None:
        assert False, ".incorepw does not exist!"

    scenario = ""
    with open("hurricanewf.json", 'r') as file:
        hurr_wf_inputs = file.read()

    response = hazardsvc.create_hurricane_windfield(hurr_wf_inputs)
    assert response["id"] is not None

def test_get_hurricanewf_values(hazardsvc):
    if hazardsvc is None:
        assert False, ".incorepw does not exist!"
    hvals = hazardsvc.get_hurricanewf_values("5bd3d6a1f242fe0cf903cb0e", "velocity",
        "kmph", ["28,-81"])

    assert (hvals[0]['hazardValue'] == 60.21153835934114)

# TODO implement the following test
# def test_get_earthquake_hazard_value_set(hazardsvc):
