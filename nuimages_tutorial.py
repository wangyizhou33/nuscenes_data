from nuimages import NuImages
import matplotlib.pyplot as plt

nuim = NuImages(dataroot='./data/nuimages-v1.0-mini', version='v1.0-mini', verbose=True, lazy=True)

print(nuim.category)
print(nuim.table_names)

sample_idx = 0
sample = nuim.sample[sample_idx]
sample = nuim.get('sample', sample['token'])
sample_idx_check = nuim.getind('sample', sample['token'])
assert sample_idx == sample_idx_check

key_camera_token = sample['key_camera_token']

nuim.render_image(key_camera_token, annotation_type='objects',  # ['all', 'surfaces', 'objects', 'none']
                  with_category=True, with_attributes=True, box_line_width=-1, render_scale=5)
plt.show()

object_tokens, surface_tokens = nuim.list_anns(sample['token'])

semantic_mask, instance_mask = nuim.get_segmentation(key_camera_token)

plt.figure(figsize=(32, 9))

plt.subplot(1, 2, 1)
plt.imshow(semantic_mask)
plt.subplot(1, 2, 2)
plt.imshow(instance_mask)
plt.show()

print(nuim.list_sample_content(sample['token']))

nuim.render_trajectory(sample['token'], rotation_yaw=0, center_key_pose=True)
plt.show()

translations, key_index = nuim.get_trajectory(sample['token'], rotation_yaw=0,
                                                center_key_pose=True)
print(translations)
print(key_index)
