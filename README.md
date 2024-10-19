# Intensity Manager

Intensity Manager could be used to manage varying intensity levels for tasks like motor control, sensor activation, or path planning, where intensity changes over time or space.

## Overview
This Python class, IntensityBySegment, allows you to manage and manipulate intensity values across various segments of a 1D number line. It supports two primary operations:
- Add: Increment or decrement intensity within a given range
- Set: Directly set the intensity within a given range

The class is designed to efficiently handle these operations using a `SortedDict` (from the `sortedcontainers` module), ensuring that points are stored in sorted order. Additionally, it ensures that overlapping or adjacent segments are properly merged or split as needed.

## Usage Example
```
# Initialize the intensity manager
intensity_manager = IntensityBySegment()

# Adding intensity to a segment
intensity_manager.add(5, 10, 3)

# Setting a fixed intensity to a segment
intensity_manager.set_value(7, 15, 5)
```
