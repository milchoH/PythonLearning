from collections import Counter

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam congue dolor sed elit tempus "\
        "sodales. Praesent ut semper dui. Integer ac ornare orci, sodales ultrices tellus. Maecenas id arcu "\
        "at ante imperdiet rhoncus. Duis ornare cursus nisl, ac condimentum magna hendrerit nec. Aenean ut turpis "\
        "ac turpis eleifend sollicitudin non finibus nunc. Quisque suscipit lorem in lacus posuere, ut tincidunt "\
        "tortor fringilla. Praesent sodales leo nec congue laoreet. Vestibulum venenatis nisl sed"\
        "dolor efficitur efficitur eu in ligula. Vestibulum pellentesque commodo neque, eu consequat ante."\
        "Phasellus libero turpis, auctor eu dignissim pulvinar, cursus non elit. Phasellus at nulla dictum, "\
        "pretium nisi non, varius ante. Phasellus congue nunc sem, ut vestibulum orci hendrerit in."\
        "Pellentesque neque eros, molestie sed sapien eget, viverra viverra sapien. Cras molestie imperdiet "\
        "tortor pellentesque molestie. Sed eget sem ante. Interdum et malesuada fames ac ante ipsum primis"\
        "in faucibus. Nulla ut vestibulum ligula. Vivamus at consectetur dolor. Morbi ut turpis at metus ornare"\
        "interdum vel sit amet erat. In vitae fringilla purus. Aliquam ultrices eros diam, ut commodo orci"\
        "mollis id."

words = text.split()

counter = Counter(words)
top_three = counter.most_common(3)
print(top_three)