#include <iostream>

int main() {
    int H, W, N;
    std::cin >> H >> W >> N;

    int ans = (N / std::max(H, W)) + std::min(1, (N % (std::max(H, W))));
    std::cout << ans << std::endl;
  
    return 0;
}