ui_data = {
    "need_fixed_passwd": False,
    "wix_login_title": "AutoAudit Login",
    "wix_login_username_label": "Email Address",
    "wix_login_password_label": "Password",
    "wix_login_button_label": "Log in",
    "wix_signup_button_label": "Or Sign Up on Our Website 🌐",
    "wix_login_error_text": "Login failed, please check your username and password.",
    "wix_signup_button_url": "https://www.example.com/",
    "wix_login_error_icon": "🚨",
    "theme": {
        "primaryColor": "#FF0000",
    },
    "page_title": "AutoAudit AI智能审计",
    "page_icon": "src/static/audit/favicon.ico",
    "page_markdown": """
      <style>
          body {
              font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol';
          }
          a {
              text-decoration: none;
          }
          a:hover {
              text-decoration: none;
          }
          div[data-testid="stDecoration"] {
              background-image: linear-gradient(90deg, #FF0000, #C2B6B2);
          }
          div[data-testid="stImage"] {
              min-width: 50px;
              max-width: 50px;
          }
          section[data-testid="stSidebar"] {
              min-width: 360px;
              max-width: 480px;
          }
          .css-164nlkn {
              text-align: right;
          }
          .thusoetext {
              width: 250px;
              height: 50px;
              background-image: url('app/static/audit/bistu_logo_new1.png');
              background-size: 250px 50px;
              background-repeat: no-repeat;
              background-position: center;
              opacity: 0.5;
          }
          .thulogo {
              width: 50px;
              height: 50px;
              background-image: url('app/static/audit/bistu_logo.png');
              background-size: 50px 50px;
              background-repeat: no-repeat;
              background-position: center;
              opacity: 0.5;
          }
          .soelogo {
              width: 50px;
              height: 50px;
              background-image: url('app/static/audit/bistu_logo.png');
              background-size: 45px 45px;
              background-repeat: no-repeat;
              background-position: center;
              opacity: 0.5;
          }
          .text-sm {
              font-size: .875rem;
              line-height: 1.25rem
          }
      </style>
      """,
    "sidebar_image": "src/static/audit/logo.png",
    "sidebar_title": "AutoAudit Chat",
    "sidebar_subheader": "AI for Audit 🔬 - 智能聊天机器人",
    "sidebar_welcome_text": """嗨，**{username}**！您当前处于**{subscription}**计划。""",
    "sidebar_markdown": """
        <div style="position: fixed; left:25px; bottom: 10px; height:110px; width: 315px; font-size: 14px; font-weight: bold; background-color: #F0F2F6;">
            <table style="border: 0; position: absolute; bottom: 35px;">
                <tr style="border: 0; width:315px; ">
                    <!--<td class="thulogo" style="border: 0;"></td>
                    <td class="soelogo" style="border: 0;"></td> -->
                    <td class="thusoetext" style="border: 0;"></td>
                </tr>
               <!-- <tr style="border: 0;">
                    <td colspan="3" style="border: 0; padding: 0;"><p class="text-sm" style="opacity: 0.5;text-align: left; margin: 0;"><a style="width: 315px; color: black; display: block" href="https://mingxu.tiangong.world" target="_blank">智能审计团队</a></p>
                    </td>
                </tr>
                -->
            </table>
            <table style="border: 0; position: absolute; bottom: 5px; width:315px;">
            <!--
                <tr style="border: 0;">
                    <td style="border: 0; text-align: center; padding: 0;"><p class="text-sm" style="margin: 0; opacity: 0.5;"><a style="color: black" href="https://ai-en.tiangong.world/">TianGong AI 🧠</a></p></td>
                    <td style="border: 0; text-align: center; padding: 0;">
                        <p class="text-sm" style="opacity: 0.5; margin: 0;"><a style="color: black" href="mailto: gpt@tiangong.world">Technical Support 📧</a></p>
                    </td>
                </tr>
                 -->
            </table>
        </div>
        """,
    "sidebar_expander_title": "高级搜索设置:",
    "search_knowledge_base_checkbox_label": "知识库",
    "search_internet_checkbox_label": "互联网",
    "search_wikipedia_checkbox_label": "维基百科",
    "search_arxiv_checkbox_label": "arXiv",
    "search_docs_checkbox_label": "文档",
    "search_docs_options": "选项:",
    "search_docs_options_isolated": "独立",
    "search_docs_options_combined": "组合",
    "sidebar_file_uploader_title": "待分析的文档：",
    "sidebar_file_uploader_spinner": "正在分析...",
    "sidebar_file_uploader_error": "所有文件都无法分析，请检查格式!",
    "sidebar_instructions": """*我是一个为学术和专业文件设计的检索增强生成（RAG）工具。我利用您在提示中提供的信息来**搜索**相关文档，然后基于这些文档生成回应。*.
### 🌟 理想问题:
1. 审计中的风险评估方法和机制是什么？
2. 如何进行高效的审计证据收集？请参考国际审计标准自2021年起的最新指导。
### 🚫 避免提问:
1. 你好!? 你能做什么?
2. 帮我写/翻译一篇审计报告。
""",
    "current_chat_title": "聊天历史：",
    "chat_ai_avatar": "src/static/audit/logo.png",
    "chat_user_avatar": "src/static/user.png",
    "chat_ai_welcome": "您好！有什么可以帮您？",
    "chat_human_placeholder": "用你喜欢的任何语言问我任何问题吧!",
    "sidebar_newchat_button_label": "新建",
    "sidebar_delete_button_label": "删除",
    "sidebar_newchat_label": "新对话",
    "chat_error_message": "哎呀，我们目前遇到了极高的访问量。请稍后再试。",
    "wix_login_wait": "请耐心等待..."
}
