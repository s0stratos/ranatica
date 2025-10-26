import re
import argparse
import sys

# Ensure UTF-8 output even on Windows
sys.stdout.reconfigure(encoding='utf-8')

def replace_short_vowel(match):
    // --- Handle <text> markup with short-vowel rule ---
    Matcher angle = Pattern.compile("<([^>]+)>").matcher(content);
    StringBuffer sb = new StringBuffer();

    while (angle.find()) {
        String inside = angle.group(1).trim();
        String lower = inside.toLowerCase();

        // ends with short vowel
        boolean endsWithShortVowel = lower.matches(".*[aeiou]$");
        // but not diphthongs
        boolean isDiphthong = lower.endsWith("ae") || lower.endsWith("au") || lower.endsWith("eu");

        String replacement;
        if (endsWithShortVowel && !isDiphthong) {
            replacement = "<em class=\"short\">" + inside + "</em>";
        } else {
            replacement = "<em>" + inside + "</em>";
        }

        angle.appendReplacement(sb, Matcher.quoteReplacement(replacement));
    }
    angle.appendTail(sb);
    content = sb.toString();

def convert_to_html_line(line):
    """
    Convert one line of annotated verse into formatted HTML.
    Expected pattern: Mer. n (meter) | verse
    """
    match = re.match(r"Ad\.\s*(\d+)\s*\(([^)]+)\)\s*\|\s*(.*)", line.strip())
    if not match:
        return ""
    num, meter, verse = match.groups()

    # Replace custom markup with HTML equivalents
    verse = re.sub(r"\[([^]]+)\]", replace_short_vowel, verse)
    verse = re.sub(r"<([^>]+)>", r"<em>\1</em>", verse)
    verse = re.sub(r"\{([^}]+)\}", r"\1", verse)  # remove braces
    verse = re.sub(r"\(([^)]+)\)", r'<span class="elis">\1</span>', verse)  # (x) → span.elis


    html = f'  <p>\nAd. {num} <span class="elis">{meter}</span> {verse} |\n  </p>'
    return html

def convert_file(input_path, output_path):
    """
    Read from raw text file and write formatted HTML.
    """
    with open(input_path, encoding="utf-8") as f:
        lines = [line for line in f if line.strip()]

    html_lines = [convert_to_html_line(line) for line in lines]
    html_content = (
        "<html>\n<head>\n<meta charset='utf-8'>\n"
        "<style>\n"
        "body { font-family: 'Times New Roman', serif; line-height: 1.6; }\n"
        "p { margin: 0.4em 0; }\n"
        ".elis { color: #555; font-style: italic; }\n"
        ".short { color: #007; font-style: italic; }\n"
        "</style>\n"
        "</head>\n<body>\n"
        + "\n".join(html_lines)
        + "\n</body>\n</html>"
    )

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"Converted {len(lines)} lines -> {output_path}")

def main():
    parser = argparse.ArgumentParser(
        description="Convert annotated Latin verse text into formatted HTML."
    )
    parser.add_argument("input", help="Path to the input text file.")
    parser.add_argument("output", help="Path to the output HTML file.")
    args = parser.parse_args()

    convert_file(args.input, args.output)

if __name__ == "__main__":
    main()


