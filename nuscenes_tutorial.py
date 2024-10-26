from nuscenes.nuscenes import NuScenes

nusc = NuScenes(version='v1.0-mini', dataroot='./data/v1.0-mini', verbose=True)

print(nusc.list_scenes())
my_scene = nusc.scene[0]
print(my_scene)

first_sample_token = my_scene['first_sample_token']
nusc.render_sample(first_sample_token)

my_sample = nusc.get('sample', first_sample_token)
print(nusc.list_sample(my_sample['token']))
