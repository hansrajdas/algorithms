/*
 * Date: 2018-07-12
 *
 * Description:
 * Draw Line: A monochrome screen is stored as a single array of bytes, allowing
 * eight consecutive pixels to be stored in one byte. The screen has width w,
 * where w is divisible by 8 (that is, no byte will be spl it across rows). The
 * height of the screen, ofcourse, can be derived from the length of the array
 * and the width . Implement a function that draws a horizontal line from
 * (xl, y) to (x2, y).
 * The method signature should look something like:
 *  drawLine(byte[] screen, int width, int Xl , int x2 , int y)
 *
 * So we are supposed to update 'screen' array to have set bits from start to
 * end of line.
 */

#include "stdio.h"

#define SCREEN_WIDTH 32
#define SCREEN_HEIGHT 16

void draw_line(unsigned char screen[], unsigned short int width,
               unsigned short int x1, unsigned short int x2,
               unsigned short int y) {
  int b = 0;
  int start_offset = x1 % 8;
  int first_full_bytes = x1 / 8;
  int end_offset = x2 % 8;
  int end_full_bytes = x2 / 8;
  unsigned char start_mask = 0x00, end_mask = 0x00, mask = 0x00;
  unsigned short int byte_number = 0;

  // Get full bytes range that we need to set.
  if (start_offset) first_full_bytes++;
  if (end_offset != 7) end_full_bytes--;

  // Set full bytes.
  for (b = first_full_bytes; b <= end_full_bytes; b++)
    // As each byte holds 8 pixels so width/8.
    screen[(width / 8) * y + b] = 0xFF;

  // Create mask for start and end of line.
  start_mask = 0xFF >> start_offset;
  end_mask = ~(0xFF >> (end_offset + 1));

  // Set start and end of line.
  if (x1/8 == x2/8) {
    mask = start_mask & end_mask;
    screen[(width / 8) * y + (x1 / 8)] |= mask;
  } else {
    if (start_offset) {
      byte_number = (width / 8) * y + first_full_bytes - 1;
      screen[byte_number] |= start_mask;
    }
    if (end_offset != 7) {
      byte_number = (width / 8) * y + end_full_bytes + 1;
      screen[byte_number] |= end_mask;
    }
  }
  
  // Printing screen byte pixels.
  for (b = 0; b < SCREEN_WIDTH * SCREEN_HEIGHT; b++)
    printf("0x%x ", screen[b]);

  printf("\n");
}

int main() {
  // Screen clean, no line drawn.
  unsigned char screen[SCREEN_WIDTH*SCREEN_HEIGHT] = {0x00};
  unsigned short int x1 = 0, x2 = 0, y = 0;

  printf("Enter starting pixel of line, x1: ");
  scanf("%hu", &x1);
  printf("Enter end pixel of line, x2: ");
  scanf("%hu", &x2);
  printf("Enter height, y: ");
  scanf("%hu", &y);
  
  // Validation.
  if ((x1 > SCREEN_WIDTH - 1) || (x2 > SCREEN_WIDTH - 1) ||
    (y > SCREEN_HEIGHT - 1)) {
    printf("Invalid input!!\n");  
    printf("Valid Range: 0 <= x1 < %d, 0 <= x2 < %d, 0 <= y < %d\n",
      SCREEN_WIDTH, SCREEN_WIDTH, SCREEN_HEIGHT);
    return -1;
  }
  draw_line(screen, SCREEN_WIDTH, x1, x2, y);
  return 0;
}
