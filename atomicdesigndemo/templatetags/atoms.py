from django import template

register = template.Library()

### Heading ###
@register.inclusion_tag("components/atoms/heading.html")
def atomHeading(text):
  return {
    "text": text,
  }

### Subheading ###
@register.inclusion_tag("components/atoms/subheading.html")
def atomSubheading(text):
  return {
    "text": text,
  }

### Paragraph ###
@register.inclusion_tag("components/atoms/paragraph.html")
def atomParagraph(text, color = "default"):
  if color not in ["default", "inverse"]:
    color = "default"
    
  return {
    "text": text,
    "color": color,
  }

### Link ###
@register.inclusion_tag("components/atoms/link.html")
def atomLink(text, url, newpage = False, disabled = False):
  return {
    "text": text,
    "url": url,
    "newpage": newpage,
    "disabled": disabled,
  }

### Button ###
@register.inclusion_tag("components/atoms/button.html")
def atomButton(text, variant = "primary", disabled = False, type = False):
  if variant not in ["primary", "secondary", "danger", "success"]:
    variant = "primary"
  if type not in ["button", "submit", "reset"]:
    type = False
  if disabled:
    variant = "disabled"

  return {
    "text": text,
    "variant": variant,
    "disabled": disabled,
    "type": type,
  }

### Label ###
@register.inclusion_tag("components/atoms/label.html")
def atomLabel(label, id = None):
  return {
    "label": label,
    "for_id": id,
  }

### Required Tag ###
@register.inclusion_tag("components/atoms/required_tag.html")
def atomRequiredTag():
  return {}

### Text Input ###
@register.inclusion_tag("components/atoms/text_input.html")
def atomTextInput(name, value = "", type = "text", placeholder = "", required = False, disabled = False, id = None, inverse = False):
  if type not in ["text", "email", "password", "date", "number"]:
    type = "text"
  if id is None: id = name
    
  return {
    "name": name,
    "value": value,
    "type": type,
    "placeholder": placeholder,
    "required": required,
    "disabled": disabled,
    "id": id,
    "inverse": inverse,
  }

### Textarea Input ###
@register.inclusion_tag("components/atoms/textarea_input.html")
def atomTextareaInput(name, value = "", placeholder = "", required = False, disabled = False, id = None):
  if id is None: id = name

  return {
    "name": name,
    "value": value,
    "placeholder": placeholder,
    "required": required,
    "disabled": disabled,
    "id": id,
  }

### Dropdown Input ###
@register.inclusion_tag("components/atoms/dropdown_input.html")
def atomDropdownInput(name, placeholder = "", required = False, disabled = False, options = [], id = None):
  if id is None: id = name
  for option in options:
    if 'selected' not in option:
      option['selected'] = False
    if 'disabled' not in option:
      option['disabled'] = False

  return {
    "name": name,
    "placeholder": placeholder,
    "required": required,
    "disabled": disabled,
    "options": options,
    "id": id,
  }

### Radio Input ###
@register.inclusion_tag("components/atoms/radio_input.html")
def atomRadioInput(name, label, value, required = False, checked = False, id = None):
  if id is None: id = name

  return {
    "name": name,
    "label": label,
    "value": value,
    "required": required,
    "checked": checked,
    "id": id,
  }

### Checkbox Input ###
@register.inclusion_tag("components/atoms/checkbox_input.html")
def atomCheckboxInput(name, label, value, required=False, checked = False, id = None):
  if id is None: id = name

  return {
    "name": name,
    "label": label,
    "value": value,
    "required": required,
    "checked": checked,
    "id": id,
  }

### Upload Input ###
@register.inclusion_tag("components/atoms/upload_input.html")
def atomUploadInput(name, multiple = False, required = False, disabled = False, id = None):
  if id is None: id = name
    
  return {
    "name": name,
    "multiple": multiple,
    "required": required,
    "disabled": disabled,
    "id": id,
  }

### Card Image ###
@register.inclusion_tag("components/atoms/card_img.html")
def atomCardImg(name, url = None):
  return {
    "name": name,
    "url": url,
  }

### Card Tag ###
@register.inclusion_tag("components/atoms/card_tag.html")
def atomCardTag(text, color = "gray"):
  if color not in ["gray", "blue", "green", "yellow", "red", "purple", "orange", "teal"]:
    color = "gray"

  return {
    "text": text,
    "color": color,
  }

### Card Title ###
@register.inclusion_tag("components/atoms/card_title.html")
def atomCardTitle(text, inverse = False):
  return {
    "text": text,
    "inverse": inverse,
  }

### Navigation Logo ###
@register.inclusion_tag("components/atoms/navigation_logo.html")
def atomNavigationLogo():
  return {}

### Navigation Item ###
@register.inclusion_tag("components/atoms/navigation_item.html")
def atomNavigationItem(name, url = "#"):
  return {
    "name": name,
    "url": url,
  }

### Message ###
@register.inclusion_tag("components/atoms/message.html")
def atomMessage(text, type = "info"):
  if type not in ["success", "error", "warning", "info"]:
    type = "info"

  return {
    "text": text,
    "type": type,
  }