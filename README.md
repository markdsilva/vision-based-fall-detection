# Vision-Based Fall Detection

> **Status: No longer maintained.** This repository preserves an old college mini project for reference and learning. No further development, bug fixes, or support are planned.

A Python computer-vision prototype that detects people in camera or video footage, estimates their body poses, and uses sequences of tracked skeleton keypoints to identify possible falls. The project also includes a desktop interface and experimental email alerts.

## How it works

1. **Person detection:** Tiny YOLOv3 locates people in each frame.
2. **Pose estimation:** an AlphaPose-derived SPPE/FastPose model estimates body keypoints.
3. **Tracking:** detections are associated across frames to build a pose history for each person.
4. **Action recognition:** a two-stream spatial-temporal graph model processes 30-frame pose sequences.
5. **Display and alerts:** the application draws skeletons, bounding boxes, and predictions, and calls an email helper when a fall is predicted.

## Repository guide

| Path | Purpose |
| --- | --- |
| `main.py` | Command-line camera/video demo with an OpenCV display |
| `App.py` | Tkinter desktop interface with a video view and action chart |
| `Detection/`, `DetectorLoader.py` | Person detection model and loader |
| `SPPE/`, `PoseEstimateLoader.py` | Pose estimation components |
| `Track/` | Tracking and pose history |
| `Actionsrecognition/`, `ActionsEstLoader.py` | Action recognition model, training code, and inference loader |
| `CameraLoader.py` | Threaded camera and video loading |
| `Models/` | Model configuration and available weight files |
| `Data/` | Dataset preparation scripts |
| `mailer.py`, `mailer2.py` | Experimental email notification helpers |

## Legacy setup notes

This is a historical snapshot, and a fresh clone is **not a ready-to-run installation**. The original environment and dependency versions were not recorded in a requirements file, and compatibility with current Python or library releases has not been verified.

The code uses Python, PyTorch, torchvision, OpenCV, NumPy, SciPy, Pillow, Matplotlib, and screeninfo. The desktop interface also requires Tkinter. Additional dependencies may be needed for dataset preparation or training.

### Email configuration

Both notification helpers read `FALL_NOTIFICATION_EMAIL` from the process environment for the configurable alert recipient and sender address. Set it to the address used by your own notification setup before running either demo. For example, in PowerShell:

```powershell
$env:FALL_NOTIFICATION_EMAIL = "your-alert-address@example.com"
```

Keep the real value outside Git. The helpers require this variable and do not load `.env` files automatically. Other legacy recipients and service settings remain in the helper scripts; review them before enabling notifications.

### Model files

The default inference paths expect:

- `Models/yolo-tiny-onecls/best-model.pth`
- `Models/yolo-tiny-onecls/yolov3-tiny-onecls.cfg`
- `Models/sppe/fast_res50_256x192.pth`
- `Models/TSSTG/tsstg-model.pth`

The ResNet-101 pose option instead expects `Models/sppe/fast_res101_320x256.pth`. The SPPE weight files are absent from this repository; `Models/sppe/info.txt` records that they were removed because of their size. Matching pose weights must be supplied before inference can run.

### Example entry points

After reconstructing a compatible environment, supplying the missing weights, and reviewing the email configuration, run commands from the repository root:

```bash
# Webcam demo
python main.py --camera 0 --device cpu

# Video-file demo (replace the path with an existing video)
python main.py --camera "path/to/video.mp4" --device cpu

# Save the annotated output
python main.py --camera "path/to/video.mp4" --device cpu --save_out "output.avi"

# Desktop interface
python App.py
```

These commands describe the existing entry points; they have not been validated as a complete installation procedure. Press `q` to close the OpenCV demo.

## Known limitations

- Some source paths and device settings are hard-coded. `App.py` needs local configuration before use, and the camera loader currently forces webcam index `0` for live-camera input.
- The checked-in action-label mapping groups several output classes under `Fall Down`; it should be reviewed before interpreting model predictions.
- Email helpers require private environment configuration, and other legacy notification settings still need review. Review or disable those helpers before running the demos; the fall-detection loop may invoke them repeatedly.
- No current accuracy benchmark or supported runtime environment is documented. This remains an academic prototype rather than a validated safety-monitoring system.

## Acknowledgments

The pose-estimation components use an AlphaPose-derived implementation, as recorded in [SPPE/README.md](SPPE/README.md). See [SPPE/LICENSE](SPPE/LICENSE) for that component's license.

## Maintenance

The project is retained as a record of college coursework. It is no longer actively developed or maintained, and issues or pull requests may not receive a response.
