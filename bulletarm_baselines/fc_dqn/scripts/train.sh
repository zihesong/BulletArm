#!/bin/bash

for ((j=-8;j>=-10;j--));do
{
    CUDA_VISIBLE_DEVICES=2 python main.py --env=object_grasping --object_index=${j}
    mv ../../../pos_info.txt ./pos_info_${j}.txt
}
done
