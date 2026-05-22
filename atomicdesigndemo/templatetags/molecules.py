from django import template

register = template.Library()

### Text Input with Label ###
@register.inclusion_tag("components/molecules/text_input_with_label.html")
def moleculeTextInputWithLabel(name, label, value = "", type = "text", placeholder = "", required = False, disabled = False, id = None):
  if id is None: id = name

  return {
    "name": name,
    "label": label,
    "value": value,
    "type": type,
    "placeholder": placeholder,
    "required": required,
    "disabled": disabled,
    "id": id,
  }

### Textarea Input with Label ###
@register.inclusion_tag("components/molecules/textarea_input_with_label.html")
def moleculeTextareaInputWithLabel(name, label, value = "", placeholder = "", required = False, disabled = False, id = None):
  if id is None: id = name

  return {
    "name": name,
    "label": label,
    "value": value,
    "placeholder": placeholder,
    "required": required,
    "disabled": disabled,
    "id": id,
  }

### Dropdown Input with Label ###
@register.inclusion_tag("components/molecules/dropdown_input_with_label.html")
def moleculeDropdownInputWithLabel(name, label, placeholder = "", required = False, disabled = False, options = [], id = None):
  if id is None: id = name

  return {
    "name": name,
    "label": label,
    "placeholder": placeholder,
    "required": required,
    "disabled": disabled,
    "options": options,
    "id": id,
  }

### Radio Input List ###
@register.inclusion_tag("components/molecules/radio_input_list.html")
def moleculeRadioInputList(name, options, label = None, required = False):
  for option in options:
    if 'checked' not in option:
      option['checked'] = False
    if 'id' not in option:
      option['id'] = f"{name}_{option['value']}"


  return {
    "name": name,
    "options": options,
    "label": label,
    "required": required,
  }

### Checkbox Input List ###
@register.inclusion_tag("components/molecules/checkbox_input_list.html")
def moleculeCheckboxInputList(name, options, label = None):
  for option in options:
    if 'checked' not in option:
      option['checked'] = False
    if 'required' not in option:
      option['required'] = False
    if 'id' not in option:
      option['id'] = f"{name}_{option['value']}"

  return {
    "name": name,
    "options": options,
    "label": label,
  }

### Upload Input with Label ###
@register.inclusion_tag("components/molecules/upload_input_with_label.html")
def moleculeUploadInputWithLabel(name, label, multiple = False, required = False, disabled = False, id = None):
  if id is None: id = name

  return {
    "name": name,
    "label": label,
    "multiple": multiple,
    "required": required,
    "disabled": disabled,
    "id": id,
  }

### Item Card ###
@register.inclusion_tag("components/molecules/item_card.html")
def moleculeItemCard(name, tags = [], url = '#', img = None):
  if img is None:
    img = "placeholder"
    
  return {
    "name": name,
    "tags": tags,
    "url": url,
    "img": f"imgs/services/{img}.png",
  }

### Search Bar ###
@register.inclusion_tag("components/molecules/search_bar.html")
def moleculeSearchBar():
  return {}