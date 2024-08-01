#include "gtest/gtest.h"

int solution();

TEST(SolutionTest, HandlesBasicInput) {
    EXPECT_EQ(solution(), 42);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
