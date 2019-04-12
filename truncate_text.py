def truncate_text(original_text, max_letters):
    if len(original_text) > max_letters:
        return original_text[:max_letters] + '...'
    else:
        return original_text

text = 'Lorem ipsum dolor sit amet, adipiscing elit. Proin convallis convallis. Quisque aliquet magna et ultrices ultrices. Nunc sed complet!'
print(truncate_text(text, 10))
print(truncate_text(text, 20))
print(truncate_text(text, 30))
print(truncate_text(text, 35))
print(truncate_text(text, 100))
print(truncate_text(text, 1000))