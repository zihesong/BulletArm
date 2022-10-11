#!/bin/bash

for ((j=-8;j<=-7;j++));do
{
    python main.py --env=object_grasping --object_index=${j}
    mv ../../../pos_info.txt ./pos_info_${j}.txt
}
done
