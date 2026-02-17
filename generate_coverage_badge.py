#!/usr/bin/env python3
"""
Generate coverage badges from pytest-cov reports.
This script reads the coverage XML report and generates SVG badges.
"""

import os
import xml.etree.ElementTree as ET


def generate_coverage_badge(coverage_percent, output_file="coverage_badge.svg"):
    """Generate an SVG coverage badge."""

    # Determine color based on coverage percentage
    if coverage_percent >= 90:
        color = "#4c1"
    elif coverage_percent >= 80:
        color = "#dfb317"
    elif coverage_percent >= 70:
        color = "#fe7d37"
    else:
        color = "#e05d44"

    # Create SVG content
    svg_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="110" height="20" role="img" aria-label="Coverage: {coverage_percent}%">
  <title>Coverage: {coverage_percent}%</title>
  <linearGradient id="s" x2="0" y2="100%">
    <stop offset="0" stop-color="#bbb" stop-opacity=".1"/>
    <stop offset="1" stop-opacity=".1"/>
  </linearGradient>
  <mask id="r">
    <rect width="110" height="20" rx="3" fill="#fff"/>
  </mask>
  <g mask="url(#r)">
    <rect width="70" height="20" fill="#555"/>
    <rect x="70" width="40" height="20" fill="{color}"/>
    <rect width="110" height="20" fill="url(#s)"/>
  </g>
  <g fill="#fff" text-anchor="middle" font-family="DejaVu Sans,Verdana,Geneva,sans-serif" font-size="11">
    <text x="35" y="15" fill="#010101" fill-opacity=".3">Coverage</text>
    <text x="35" y="14">Coverage</text>
    <text x="95" y="15" fill="#010101" fill-opacity=".3">{coverage_percent}%</text>
    <text x="95" y="14">{coverage_percent}%</text>
  </g>
</svg>'''

    # Write SVG file
    with open(output_file, "w") as f:
        f.write(svg_content)

    print(f"Generated coverage badge: {output_file} ({coverage_percent}%)")
    return output_file

def parse_coverage_xml(xml_file="coverage.xml"):
    """Parse coverage.xml file to extract coverage percentage."""

    if not os.path.exists(xml_file):
        print(f"Error: Coverage file {xml_file} not found.")
        print("Please run pytest with coverage first:")
        print("  pytest --cov=pyquantity --cov-report=xml")
        return None

    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()

        # Find coverage percentage
        coverage_percent = None
        for elem in root.iter():
            if 'line-rate' in elem.attrib:
                coverage_percent = float(elem.attrib['line-rate']) * 100
                break

        if coverage_percent is None:
            print("Error: Could not find coverage percentage in XML file.")
            return None

        return round(coverage_percent, 1)

    except ET.ParseError as e:
        print(f"Error parsing XML file: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

def main():
    """Main function to generate coverage badge."""

    # Parse coverage from XML report
    coverage_percent = parse_coverage_xml()

    if coverage_percent is None:
        return 1

    # Generate badge
    generate_coverage_badge(coverage_percent)

    # Also generate a simple text badge for README
    with open("COVERAGE.txt", "w") as f:
        f.write(f"Current test coverage: {coverage_percent}%")

    print(f"Coverage: {coverage_percent}%")
    print("Badge generated successfully!")

    return 0

if __name__ == "__main__":
    exit(main())

