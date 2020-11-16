# from rest_framework import permissions
#
# class AdminPermission(permissions.BasePermission):
#
#     def has_permission(self, request, view):
#         if view.action in ['retrieve', 'destroy']:
#             return request.user.is_authenticated
#         elif view.action in ['list','create', 'partial_update' , 'update']:
#             return True
#         else:
#             return False
#
#     def has_object_permission(self, request, view, obj):
#         # Deny actions on objects if the user is not authenticated
#         if not request.user.is_authenticated:
#             return False
#
#         if view.action == 'retrieve':
#             return obj == request.user or request.user.is_authenticated
#         elif view.action == 'destroy':
#             return request.user.is_authenticated
#         else:
#             return False
