import pybullet as pb
import numpy as np
import random
import os
import glob
import pyredner # pyredner will be the main Python module we import for redner.
import torch # We also import PyTorch
import urllib
import zipfile
import random
import torchvision
import math
from typing import Optional, List

class Sensor(object):
  def __init__(self, cam_pos, cam_up_vector, target_pos, target_size, near, far):
    self.view_matrix = pb.computeViewMatrix(
      cameraEyePosition=cam_pos,
      cameraUpVector=cam_up_vector,
      cameraTargetPosition=target_pos,
    )
    
    self.cam_pos = cam_pos
    self.cam_up_vector = cam_up_vector
    self.target_pos = target_pos
    self.near = near
    self.far = far
    self.fov = np.degrees(2 * np.arctan((target_size / 2) / self.far))
    self.proj_matrix = pb.computeProjectionMatrixFOV(self.fov, 1, self.near, self.far)

  def setCamMatrix(self, cam_pos, cam_up_vector, target_pos):
    self.view_matrix = pb.computeViewMatrix(
      cameraEyePosition=[cam_pos[0], cam_pos[1], cam_pos[2]],
      cameraUpVector=cam_up_vector,
      cameraTargetPosition=target_pos,
    )
    self.proj_matrix = pb.computeProjectionMatrixFOV(70, 1, 0.001, 0.3)



  def getHeightmap(self, size, objs):

    def setPosition(position: List[float] = None):
      dir = "/Users/tingxi/_BulletArm/BulletArm/bulletarm/pybullet/urdf/object/GraspNet1B_object/003/convex.obj"
      obj = pyredner.load_obj(dir, return_objects=True)
      newObj = obj[0]
      d_x, d_y, d_z = position[0], position[1], position[2]
      newObj.vertices += torch.tensor([d_x, d_y, d_z])
      return newObj

    def rendering(cam_pos, cam_up_vector, target_pos, obj_list):
      
      cam_pos = torch.FloatTensor(cam_pos)
      cam_up_vector = torch.FloatTensor(cam_up_vector)
      target_pos = torch.FloatTensor(target_pos)

      camera = pyredner.Camera(position = cam_pos,
                          look_at = target_pos,
                          up = cam_up_vector,
                          fov = torch.tensor([30.0]), # in degree
                          clip_near = 1e-2, # needs to > 0
                          resolution = (128, 128)
                          )
      
      scene = pyredner.Scene(camera = camera, objects = obj_list)
      chan_list = [pyredner.channels.depth]
      img = pyredner.render_generic(scene, chan_list)

      return img.numpy()  
    
    #image_arr = pb.getCameraImage(width=size, height=size,
    #                              viewMatrix=self.view_matrix,
    #                              projectionMatrix=self.proj_matrix,
    #                              renderer=pb.ER_TINY_RENDERER)
    #depth_img = np.array(image_arr[3])
    #depth = self.far * self.near / (self.far - (self.far - self.near) * depth_img)

    #position = [0.03, 0.03, 0.0]
    obj_list = []

    for _ in objs:
      p = random.uniform(-1.0, 1.0)
      p = torch.tensor([p, p, 0])
      newObj = setPosition(p)
      obj_list.append(newObj)

      #f=open("../../pos_info.txt","a")
      #f.write("object_index: " + str(obj) + ", pos: " + str(p) + "\n")
    #img = rendering(cameraEyePosition, cameraUpVector, cameraTargetPosition, obj_list)
    #return np.abs(depth - np.max(depth)).reshape(size, size)

    img = rendering(self.cam_pos, self.cam_up_vector, self.target_pos, obj_list)

    return img

  def getRGBImg(self, size, objs):
    # image_arr = pb.getCameraImage(width=size, height=size,
    #                               viewMatrix=self.view_matrix,
    #                               projectionMatrix=self.proj_matrix,
    #                               renderer=pb.ER_TINY_RENDERER)
    # rgb_img = np.moveaxis(image_arr[2][:, :, :3], 2, 0) / 255
    def setPosition(position: List[float] = None):
      dir = "/Users/tingxi/_BulletArm/BulletArm/bulletarm/pybullet/urdf/object/GraspNet1B_object/003/convex.obj"
      obj = pyredner.load_obj(dir, return_objects=True)
      newObj = obj[0]
      d_x, d_y, d_z = position[0], position[1], position[2]
      newObj.vertices += torch.tensor([d_x, d_y, d_z])
      return newObj

    def rendering(cam_pos, cam_up_vector, target_pos, obj_list):
      
      cam_pos = torch.FloatTensor(cam_pos)
      cam_up_vector = torch.FloatTensor(cam_up_vector)
      target_pos = torch.FloatTensor(target_pos)

      camera = pyredner.Camera(position = cam_pos,
                          look_at = target_pos,
                          up = cam_up_vector,
                          fov = torch.tensor([30.0]), # in degree
                          clip_near = 1e-2, # needs to > 0
                          resolution = (128, 128)
                          )
      
      scene = pyredner.Scene(camera = camera, objects = obj_list)
      rgb_img = pyredner.render_albedo(scene, alpha=False)
      return rgb_img.numpy()  
    
    obj_list = []

    for _ in objs:
      p = random.uniform(-1.0, 1.0)
      p = torch.tensor([p, p, 0])
      newObj = setPosition(p)
      obj_list.append(newObj)
    rgb_img = rendering(self.cam_pos, self.cam_up_vector, self.target_pos, obj_list)
    return rgb_img

  def getDepthImg(self, size):
    image_arr = pb.getCameraImage(width=size, height=size,
                                  viewMatrix=self.view_matrix,
                                  projectionMatrix=self.proj_matrix,
                                  renderer=pb.ER_TINY_RENDERER)
    depth_img = np.array(image_arr[3])
    depth = self.far * self.near / (self.far - (self.far - self.near) * depth_img)
    return depth.reshape(size, size)

  def getPointCloud(self, size, to_numpy=True):
    image_arr = pb.getCameraImage(width=size, height=size,
                                  viewMatrix=self.view_matrix, 
                                  projectionMatrix=self.proj_matrix, 
                                  renderer=pb.ER_TINY_RENDERER)
    depthImg = np.asarray(image_arr[3])

    # https://stackoverflow.com/questions/59128880/getting-world-coordinates-from-opengl-depth-buffer
    projectionMatrix = np.asarray(self.proj_matrix).reshape([4,4],order='F')
    viewMatrix = np.asarray(self.view_matrix).reshape([4,4],order='F')
    tran_pix_world = np.linalg.inv(np.matmul(projectionMatrix, viewMatrix))
    pixel_pos = np.mgrid[0:size, 0:size]
    pixel_pos = pixel_pos/(size/2) - 1
    pixel_pos = np.moveaxis(pixel_pos, 1, 2)
    pixel_pos[1] = -pixel_pos[1]
    zs = 2*depthImg.reshape(1, size, size) - 1
    pixel_pos = np.concatenate((pixel_pos, zs))
    pixel_pos = pixel_pos.reshape(3, -1)
    augment = np.ones((1, pixel_pos.shape[1]))
    pixel_pos = np.concatenate((pixel_pos, augment), axis=0)
    position = np.matmul(tran_pix_world, pixel_pos)
    pc = position / position[3]
    points = pc.T[:, :3]

    # if to_numpy:
      # points = np.asnumpy(points)
    return points
