import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useUserStore = defineStore(
  'user',
  () => {
    // 直接赋值，没有返回函数的方式修改
    let LoginVisibility = ref(false) // 登录框是否显示
    let Nickname = ref(null)
    let Email = ref(null)
    let Edit = ref(false) // 是否是编辑状态
    let EditIconDisabled = ref(true) // 是否显示编辑图标

    return {
      LoginVisibility,
      Nickname,
      Email,
      Edit,
      EditIconDisabled
    }
  },
  {
    persist: {
      paths: ['Nickname', 'Email']
    }
  }
)
