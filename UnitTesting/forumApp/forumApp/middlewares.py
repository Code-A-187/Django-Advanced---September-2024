import time

from django.utils.deprecation import MiddlewareMixin


def measure_time_execution(get_response):
    def middleware(request, *args, **kwargs):
        start_time = time.time()
        response = get_response(request)  # executes middleware or the view
        end_time = time.time()

        print(f"Total time needed for execution was {end_time - start_time}")

        return response

    return middleware


# class MeasureTimeExecution:
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request, *args, **kwargs):
#         start_time = time.time()
#         response = self.get_response(request)  # executes middleware or the view
#         end_time = time.time()
#
#         print(f"Total time needed for execution witch Class was {end_time - start_time}")
#
#         return response


class MeasureTimeExecution(MiddlewareMixin):
    def process_request(self, request):
        self.start_time = time.time()

    def process_view(self, request, view, *args, **kwargs):
        print("It's processing")

    def process_template_response(self, request, response):
        print(f"It's processing template response")
        return response

    def process_exception(self, request, exception):
        print(f"the exeption that happened was {exception}")

    def process_response(self, request, response):
        self.end_time = time.time()
        total_time = self.end_time - self.start_time
        print(f'New class measure time: {total_time}')
        return response
