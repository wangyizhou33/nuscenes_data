# Read me

### 1.Store raw data in ./data
download from https://motional-nuscenes.s3.ap-northeast-1.amazonaws.com/index.html

NuImages file tree looks like
```txt
data/
└── nuimages-v1.0-mini
    ├── LICENSE
    ├── samples
    │   ├── CAM_BACK
    │   ├── CAM_BACK_LEFT
    │   ├── CAM_BACK_RIGHT
    │   ├── CAM_FRONT
    │   ├── CAM_FRONT_LEFT
    │   └── CAM_FRONT_RIGHT
    ├── sweeps
    │   ├── CAM_BACK
    │   ├── CAM_BACK_LEFT
    │   ├── CAM_BACK_RIGHT
    │   ├── CAM_FRONT
    │   ├── CAM_FRONT_LEFT
    │   └── CAM_FRONT_RIGHT
    └── v1.0-mini
        ├── attribute.json
        ├── calibrated_sensor.json
        ├── category.json
        ├── ego_pose.json
        ├── log.json
        ├── object_ann.json
        ├── sample_data.json
        ├── sample.json
        ├── sensor.json
        └── surface_ann.json
```

NuScenes file tree looks like
```
data/
└── v1.0-mini/
    ├── LICENSE
    ├── maps
    │   ├── 36092f0b03a857c6a3403e25b4b7aab3.png
    │   ├── 37819e65e09e5547b8a3ceaefba56bb2.png
    │   ├── 53992ee3023e5494b90c316c183be829.png
    │   └── 93406b464a165eaba6d9de76ca09f5da.png
    ├── samples
    │   ├── CAM_BACK
    │   ├── CAM_BACK_LEFT
    │   ├── CAM_BACK_RIGHT
    │   ├── CAM_FRONT
    │   ├── CAM_FRONT_LEFT
    │   ├── CAM_FRONT_RIGHT
    │   ├── LIDAR_TOP
    │   ├── RADAR_BACK_LEFT
    │   ├── RADAR_BACK_RIGHT
    │   ├── RADAR_FRONT
    │   ├── RADAR_FRONT_LEFT
    │   └── RADAR_FRONT_RIGHT
    ├── sweeps
    │   ├── CAM_BACK
    │   ├── CAM_BACK_LEFT
    │   ├── CAM_BACK_RIGHT
    │   ├── CAM_FRONT
    │   ├── CAM_FRONT_LEFT
    │   ├── CAM_FRONT_RIGHT
    │   ├── LIDAR_TOP
    │   ├── RADAR_BACK_LEFT
    │   ├── RADAR_BACK_RIGHT
    │   ├── RADAR_FRONT
    │   ├── RADAR_FRONT_LEFT
    │   └── RADAR_FRONT_RIGHT
    └── v1.0-mini
        ├── attribute.json
        ├── calibrated_sensor.json
        ├── category.json
        ├── ego_pose.json
        ├── instance.json
        ├── log.json
        ├── map.json
        ├── sample_annotation.json
        ├── sample_data.json
        ├── sample.json
        ├── scene.json
        ├── sensor.json
        └── visibility.json
```

### 2. get git-submodule
update using `git submodule update --init`

