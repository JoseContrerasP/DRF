from rest_framework import permissions

class IsStaffEditorPermission(permissions.DjangoModelPermissions):
	# this is a better way to give permissions because, now we're able to give specifics permissions, on the contrary the previous has_permissions when we give the users one permissions, he can do everything 
	perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'], # seems similar to how we manage variables in a make file 
        'PUT': ['%(app_label)s.change_%(model_name)s'], # Also seems similar to the format we had used in the products.models.sale_price 
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

	# def has_permission(self, request, view):

	# 	if not request.user.is_staff:
	# 		return False
	# 	return super().has_permission(request, view)

	# def has_permission(self, request, view):
	# 	user = request.user
	# 	print(user.get_all_permissions())
	# 	if user.is_staff:
	# 		if user.has_perm("products.view_products"):
	# 			return True
	# 		if user.has_perm("products.add_products"):
	# 			return True
	# 		if user.has_perm("products.change_products"):
	# 			return True
	# 		if user.has_perm("products.delete_products"):
	# 			return True

	# 		return False

	# 	return False
