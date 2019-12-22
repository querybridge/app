from django.utils.text import slugify

def get_unique_slug_product(model_instance, slugable_field_name, slug_field_name):
    slug = slugify(getattr(model_instance, slugable_field_name))
    unique_slug = slug
    extension = 1
    ModelClass = model_instance.__class__

    while ModelClass._default_manager.filter(
        **{slug_field_name: unique_slug}
    ).exists():
        unique_slug = '{}-{}'.format(slug, extension)
        extension += 1
    return unique_slug

def get_unique_slug_inventory(model_instance, slugable_field_name, slug_field_name):
    slug = slugify(getattr(model_instance, slugable_field_name))
    unique_slug = slug
    extension = 1
    ModelClass = model_instance.__class__

    while ModelClass._default_manager.filter(
        **{slug_field_name: unique_slug}
    ).exists():
        unique_slug = '{}-{}'.format(slug, extension)
        extension += 1
    return unique_slug


## DROPDOWN FIELD VALUES
COLOR_CHOICES = [
    ('BLACK','black'),
    ('SILVER','silver'),
    ('GRAY','gray'),
    ('GOLD','gold'),
    ('ROSE GOLD','rose gold'),
    ('BRONZE','bronze'),
    ('COPPER','copper'),
    ('WHITE','white'),
    ('DARK RED','dark red'),
    ('RED','red'),
    ('PURPLE','purple'),
    ('PINK','pink'),
    ('GREEN','green'),
    ('NEON GREEN','neon green'),
    ('ARMY GREEN','army green'),
    ('YELLOW','yellow'),
    ('DARK BLUE','dark blue'),
    ('SEA GREEN','sea green'),
    ('SEA BLUE','sea blue'),
]

FINISH_CHOICES = [
    ('MATTE','matte'),
    ('SATIN','satin'),
    ('GLOSS','gloss'),
    ('MIRROR','mirror'),
    ('MILLED','milled'),
]
