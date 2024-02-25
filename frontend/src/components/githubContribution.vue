<template>
  <div class="container">
    <div v-if="loading" class="loading-container">
      <div class="loading-spinner"></div>
    </div>

    <div class="container-main" v-else>
      <div
        v-for="(weeks, weekIndex) in datas?.weeks"
        :key="weekIndex"
        class="weeks"
      >
        <div v-for="cell in weeks.contributionDays" :key="cell.firstDay">
          <!-- <el-tooltip
            class="box-item"
            effect="dark"
            :content="`${cell.contributionCount === 0 ? 'No contribution' : cell.contributionCount + ' contributions'} on ${cell.date}`"
            placement="top"
          > -->
          <div
            class="cell"
            :data-tip="`${cell.contributionCount === 0 ? 'No contribution' : cell.contributionCount + ' contributions'} on ${cell.date}`"
            :style="{ backgroundColor: cell.color }"
            @mouseenter="
              showTooltipHandler($event, cell.contributionCount, cell.date)
            "
            @mouseleave="tooltip_visible = false"
          ></div>
          <!-- </el-tooltip> -->
        </div>
      </div>

      <!-- tooltip 组件 -->
      <div
        v-show="tooltip_visible"
        class="tooltip"
        :style="{ top: tooltip_top + 'px', left: tooltip_left + 'px' }"
      >
        {{ tooltip_content }}
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { githubApiKey, githubName } from '/secret.js'
import { getGithubContributions } from '@/api/github.js'

let datas = null
const loading = ref(true)

const tooltip_visible = ref(false)
const tooltip_top = ref(0)
const tooltip_left = ref(0)
const tooltip_content = ref('')

;(async () => {
  console.log('hello GithubContribution.vue')
  try {
    const { data } = await getGithubContributions(githubName, githubApiKey)
    datas = data.data.user.contributionsCollection.contributionCalendar
    console.log(datas)
  } catch (error) {
    console.error('Error fetching data:', error)
  } finally {
    // 数据加载完成后，隐藏 loading
    loading.value = false
  }
})()

const showTooltipHandler = (event, contributionCount, date) => {
  const rect = event.target.getBoundingClientRect() // 获取元素位置信息
  tooltip_top.value = rect.top // 垂直方向：不要中心点，就要上表面
  tooltip_left.value = (rect.left + rect.right) / 2 // 水平方向：中心点
  tooltip_content.value = `${contributionCount === 0 ? 'No contribution' : contributionCount + ' ' + (contributionCount === 1 ? 'contribution' : 'contributions')} on ${date}`
  tooltip_visible.value = true
}
</script>

<style scoped>
.container-main {
  display: flex;
  justify-content: center;
  align-items: flex-start;
  background-color: #fff;
  overflow-x: auto;
}

.weeks {
  display: flex;
  flex-direction: column;
}

.cell {
  width: 16px;
  height: 18px;
  margin: 2px;
  box-shadow: 0 2px 2px rgba(0, 0, 0, 0.1);
}

.cell:hover {
  transform: scale(1.1);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.tooltip {
  /* content: attr(data-tip); */
  background-color: #333;
  color: white;
  position: fixed;
  padding: 4px 10px;
  /* top: 604px;
  left: 316px; */
  transform: translate(-50%, calc(-100% - 5px));
  border-radius: 5px;
  white-space: nowrap; /* 不换行 */
}

.tooltip::before {
  content: '';
  background-color: #333;
  position: absolute;
  width: 8px;
  height: 8px;
  bottom: 0;
  left: 50%;
  transform: translate(-50%, calc(100% - 4px)) rotate(45deg);
}

.loading-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 150px; /* 或者根据实际需要设置 */
}

.loading-spinner {
  border: 8px solid rgba(0, 0, 0, 0.1);
  border-top: 8px solid #007bff; /* Loading 颜色可以根据需要调整 */
  border-radius: 50%;
  width: 40px;
  height: 40px;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style>
