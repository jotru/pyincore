from pyincore import InsecureIncoreClient
from pyincore.analyses.waterfacilitydamage import WaterFacilityDamage

def run_with_base_class():
    client = InsecureIncoreClient("http://incore2-services.ncsa.illinois.edu:8888", "incrtest")
    hazard_type = "earthquake"
    hazard_id = "5b902cb273c3371e1236b36b"
    facility_datasetid = "5a284f2ac7d30d13bc081e52"

    mapping_id = "5b47c3b1337d4a387e85564b"  # Hazus Potable Water Facility Fragility Mapping - Only PGA
    #mapping_id = "5b47c383337d4a387669d592" #Potable Water Facility Fragility Mapping for INA - Has PGD

    liq_geology_dataset_id = None
    liq_geology_dataset_id =  "5a284f53c7d30d13bc08249c"

    uncertainty = False

    wf_dmg = WaterFacilityDamage(client)
    wf_dmg.load_remote_input_dataset("water_facilities", facility_datasetid)

    result_name = "wf-dmg-results.csv"
    wf_dmg.set_parameter("result_name", result_name)

    wf_dmg.set_parameter("hazard_type", hazard_type)
    wf_dmg.set_parameter("hazard_id", hazard_id)
    wf_dmg.set_parameter("mapping_id", mapping_id)
    wf_dmg.set_parameter("fragility_key", "pga")
    wf_dmg.set_parameter("liquefaction_geology_dataset_id", liq_geology_dataset_id)
    wf_dmg.set_parameter("use_hazard_uncertainty", uncertainty)
    wf_dmg.set_parameter("num_cpu", 4)

    wf_dmg.run_analysis()

if __name__ == '__main__':
    # client = InsecureIncoreClient("http://incore2-services.ncsa.illinois.edu:8888", "incrtest")
    # wf_dmg = WaterFacilityDamage(client)
    # specs = wf_dmg.get_spec()
    # print(specs)

    run_with_base_class()

