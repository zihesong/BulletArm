#!/bin/bash

# for ((i=1;i<16;i++));do
# {
#     python test.py --load_model_pre='/home/zoooe/workspaces/BulletArm/bulletarm_baselines/fc_dqn/scripts/output/margin_asr_equ_resu_df_flip_object_grasping/2022-09-19.18:34:35/models/snapshot' --env=object_grasping --num_objects=${i}
# }
# done

# for ((j=0;j<8;j++));do
# {
#     python test.py --load_model_pre='/home/mxh170530/BulletArm/bulletarm_baselines/fc_dqn/scripts/output/margin_asr_equ_resu_df_flip_object_grasping/2022-10-10.20:06:28/models/snapshot' --env=object_grasping --object_index=${j}
# }
# done


# for ((j=8;j<17;j++));do
# {
#     python test.py --load_model_pre='/home/mxh170530/BulletArm/bulletarm_baselines/fc_dqn/scripts/output/margin_asr_equ_resu_df_flip_object_grasping/2022-10-11.07:22:47/models/snapshot' --env=object_grasping --object_index=${j}
# }
# done

# for ((j=17;j<25;j++));do
# {
#     python test.py --load_model_pre='/home/mxh170530/BulletArm/bulletarm_baselines/fc_dqn/scripts/output/margin_asr_equ_resu_df_flip_object_grasping/2022-10-11.18:53:52/models/snapshot' --env=object_grasping --object_index=${j}
# }
# done


for ((j=25;j<34;j++));do
{
    python test.py --load_model_pre='/home/mxh170530/BulletArm/bulletarm_baselines/fc_dqn/scripts/output/margin_asr_equ_resu_df_flip_object_grasping/2022-10-14.12:32:11/models/snapshot' --env=object_grasping --object_index=${j}
}
done


for ((j=34;j<43;j++));do
{
    python test.py --load_model_pre='/home/mxh170530/BulletArm/bulletarm_baselines/fc_dqn/scripts/output/margin_asr_equ_resu_df_flip_object_grasping/2022-10-15.07:20:19/models/snapshot' --env=object_grasping --object_index=${j}
}
done


for ((j=43;j<51;j++));do
{
    python test.py --load_model_pre='/home/mxh170530/BulletArm/bulletarm_baselines/fc_dqn/scripts/output/margin_asr_equ_resu_df_flip_object_grasping/2022-10-16.02:36:10/models/snapshot' --env=object_grasping --object_index=${j}
}
done


for ((j=51;j<60;j++));do
{
    python test.py --load_model_pre='/home/mxh170530/BulletArm/bulletarm_baselines/fc_dqn/scripts/output/margin_asr_equ_resu_df_flip_object_grasping/2022-10-16.21:44:43/models/snapshot' --env=object_grasping --object_index=${j}
}
done


for ((j=60;j<68;j++));do
{
    python test.py --load_model_pre='/home/mxh170530/BulletArm/bulletarm_baselines/fc_dqn/scripts/output/margin_asr_equ_resu_df_flip_object_grasping/2022-10-17.16:34:17/models/snapshot' --env=object_grasping --object_index=${j}
}
done