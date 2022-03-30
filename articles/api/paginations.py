from drf_multiple_model.pagination import MultipleModelLimitOffsetPagination



class LimitPagination(MultipleModelLimitOffsetPagination):
    default_limit = 4

class LimitPaginationArticles(MultipleModelLimitOffsetPagination):
    default_limit = 9