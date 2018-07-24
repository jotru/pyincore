
class PipelineUtil:
    """
            Utility methods for pipeline analysis
    """

    @staticmethod
    def convert_result_unit(result_unit: str, result: float):
        if result_unit.lower() == "repairs/km":
            return result
        elif result_unit.lower() == "repairs/1000ft":
            return result / 0.3048

        print("Result type was not found so we didn't change it.  For pipes, all results should convert from their unit \
              type into Repairs per Kilometer for uniform results.  We found a result type of " + result_unit)
        return result

    @staticmethod
    def get_pipe_length(pipeline):
        pipe_length = 0.0

        if 'pipelength' in pipeline['properties']:
            pipe_length = float(pipeline['properties']['pipelength'])
        elif 'length_km' in pipeline['properties']:
            pipe_length = float(pipeline['properties']['length_km'])
        elif 'length' in pipeline['properties']:
            pipe_length = float(pipeline['properties']['length'])
        else:
            print("Pipeline has no length attribute")

        return pipe_length

    @staticmethod
    def get_pipe_diameter(pipeline):
        diameter = 0.0
        if 'diameter' in pipeline['properties']:
            diameter = float(pipeline['properties']['diameter'])

        return diameter
