from rest_framework.throttling import UserRateThrottle


class Pawan_Rate_Throttle(UserRateThrottle):
    scope = 'pawan'