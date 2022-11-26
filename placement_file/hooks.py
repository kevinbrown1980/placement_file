from . import __version__ as app_version

app_name = "placement_file"
app_title = "Placement File"
app_publisher = "Kevin Brown"
app_description = "Digital Placement File"
app_email = "kevin.brown@infinics.co.uk"
app_license = "MIT"
app_logo_url = "/assets/placement_file/images/our-family.png"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/placement_file/css/placement_file.css"
# app_include_js = "/assets/placement_file/js/placement_file.js"

# include js, css files in header of web template
# web_include_css = "/assets/placement_file/css/placement_file.css"
# web_include_js = "/assets/placement_file/js/placement_file.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "placement_file/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

website_context = {
	"favicon": 	"/assets/placement_file/images/our-family.png",
	"splash_image": "/assets/placement_file/images/our-family.png"
}

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "placement_file.utils.jinja_methods",
#	"filters": "placement_file.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "placement_file.install.before_install"
# after_install = "placement_file.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "placement_file.uninstall.before_uninstall"
# after_uninstall = "placement_file.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "placement_file.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"placement_file.tasks.all"
#	],
#	"daily": [
#		"placement_file.tasks.daily"
#	],
#	"hourly": [
#		"placement_file.tasks.hourly"
#	],
#	"weekly": [
#		"placement_file.tasks.weekly"
#	],
#	"monthly": [
#		"placement_file.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "placement_file.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "placement_file.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "placement_file.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"placement_file.auth.validate"
# ]
