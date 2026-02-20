# from settings.models import Favicon, Logo, SiteInfo, SocialLinks, PageBanner
# from footer.models import UsefulLinks, CopyrightText
# from pages.models import *
# from howwedo.models import HowWeDo
# from popup.models import Popup
# from services.models import Services
# # from clients.models import Client


# def default(request):
#     favicon = Favicon.objects.first()
#     logo = Logo.objects.first()
#     company_info = SiteInfo.objects.first()
#     social_links = SocialLinks.objects.first()
#     banner = PageBanner.objects.first()
#     useful_links = UsefulLinks.objects.all().order_by('serial_no')
#     copyright_text = CopyrightText.objects.first()
#     howwedo_all=HowWeDo.objects.all()
#     pages = Page.objects.all()
#     popups = Popup.objects.first()

#     all_services = Services.objects.all().order_by('ordering')
#     # clients = Client.objects.all()
#     return {
#         'favicon': favicon,
#         'logo': logo,
#         'company_info': company_info,
#         'banner': banner,
#         'social_links': social_links,
#         'useful_links': useful_links,
#         'copyright_text': copyright_text,
#         'howwedo_all': howwedo_all,
#         'pages': pages,
#         'popups': popups,

#         'all_services': all_services,
#         # 'clients': clients,
#     }
