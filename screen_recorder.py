import pyautogui
import cv2
import numpy as np
import time
import sys
from datetime import datetime

def get_screen_resolution():
    """Get the actual screen resolution"""
    try:
        screen_size = pyautogui.size()
        return screen_size.width, screen_size.height
    except Exception as e:
        print(f"Error getting screen resolution: {e}")
        return 1920, 1080  # Default fallback

def create_video_writer(filename, fps, resolution):
    """Create and validate video writer"""
    # Try different codecs in order of preference
    codecs = [
        cv2.VideoWriter_fourcc(*"mp4v"),
        cv2.VideoWriter_fourcc(*"XVID"),
        cv2.VideoWriter_fourcc(*"MJPG"),
        cv2.VideoWriter_fourcc(*"X264")
    ]
    
    for codec in codecs:
        out = cv2.VideoWriter(filename, codec, fps, resolution)
        if out.isOpened():
            print(f"Successfully created video writer with codec")
            return out
        out.release()
    
    raise Exception("Could not create video writer with any codec")

def main():
    # Get actual screen resolution
    screen_width, screen_height = get_screen_resolution()
    print(f"Detected screen resolution: {screen_width}x{screen_height}")
    
    # Use actual screen resolution
    resolution = (screen_width, screen_height)
    
    # Generate timestamped filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"Screen_record_{timestamp}.mp4"
    
    # Reduced FPS for better performance
    fps = 15.0
    
    # Disable pyautogui fail-safe (optional - remove if you want fail-safe)
    pyautogui.FAILSAFE = True
    
    # Create video writer with error handling
    try:
        out = create_video_writer(filename, fps, resolution)
    except Exception as e:
        print(f"Failed to create video writer: {e}")
        return
    
    # Create display window (smaller for performance)
    display_width = min(800, screen_width // 2)
    display_height = min(600, screen_height // 2)
    
    cv2.namedWindow("Live Recording", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Live Recording", display_width, display_height)
    
    print(f"Starting screen recording...")
    print(f"Output file: {filename}")
    print(f"Resolution: {resolution}")
    print(f"FPS: {fps}")
    print("Press 'q' to stop recording")
    
    frame_count = 0
    start_time = time.time()
    
    try:
        while True:
            try:
                # Take screenshot
                img = pyautogui.screenshot()
                
                # Convert to numpy array
                frame = np.array(img)
                
                # Convert RGB to BGR for OpenCV
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
                
                # Verify frame dimensions match expected resolution
                if frame.shape[1] != resolution[0] or frame.shape[0] != resolution[1]:
                    print(f"Warning: Frame size mismatch. Expected {resolution}, got {frame.shape[1]}x{frame.shape[0]}")
                    # Resize frame to match expected resolution
                    frame = cv2.resize(frame, resolution)
                
                # Write frame to video
                success = out.write(frame)
                if not success:
                    print("Warning: Failed to write frame to video")
                
                # Create smaller frame for display
                display_frame = cv2.resize(frame, (display_width, display_height))
                
                # Add recording indicator
                cv2.putText(display_frame, f"REC {frame_count}", (10, 30), 
                           cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                
                # Display frame
                cv2.imshow("Live Recording", display_frame)
                
                frame_count += 1
                
                # Check for quit key
                key = cv2.waitKey(1) & 0xFF
                if key == ord('q'):
                    break
                elif key == ord('p'):  # Pause/resume functionality
                    print("Recording paused. Press any key to resume...")
                    cv2.waitKey(0)
                    
            except Exception as e:
                print(f"Error capturing frame {frame_count}: {e}")
                # Continue recording despite individual frame errors
                continue
                
    except KeyboardInterrupt:
        print("\nRecording interrupted by user")
    except Exception as e:
        print(f"Critical error during recording: {e}")
    
    finally:
        # Ensure proper cleanup
        try:
            out.release()
        except:
            pass
        
        try:
            cv2.destroyAllWindows()
        except:
            pass
        
        # Calculate and display statistics
        end_time = time.time()
        duration = end_time - start_time
        actual_fps = frame_count / duration if duration > 0 else 0
        
        print(f"\nRecording stopped!")
        print(f"Video saved as: {filename}")
        print(f"Total frames recorded: {frame_count}")
        print(f"Recording duration: {duration:.2f} seconds")
        print(f"Average FPS: {actual_fps:.2f}")

if __name__ == "__main__":
    main()