#include "example.hpp"

#include <gtest/gtest.h>

TEST(example, itWorks)
{
    EXPECT_EQ(3, {{name}}::Add(1, 2));
}
