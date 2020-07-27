import textwrap

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(max_width)
    word_list = wrapper.wrap(text=string)
    return '\n'.join(word_list)



if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)