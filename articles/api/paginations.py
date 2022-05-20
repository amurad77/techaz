from drf_multiple_model.pagination import MultipleModelLimitOffsetPagination



class LimitPagination(MultipleModelLimitOffsetPagination):
    default_limit = 10

class LimitPaginationArticles(MultipleModelLimitOffsetPagination):
    default_limit = 9

class LimitPaginationSearch(MultipleModelLimitOffsetPagination):
    default_limit = 15