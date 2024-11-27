document.addEventListener("DOMContentLoaded", () => {
    const modal = document.getElementById("modal");
    const closeButton = document.querySelector(".close-button");
    const moreButton = document.getElementById("moreButton");
    const additionalInfo = document.getElementById("additionalInfo");

    // 모달 열기
    document.querySelectorAll(".syn-alert").forEach((synAlert) => {
        synAlert.addEventListener("click", function() {
            modal.style.display = "block"; // 모달을 표시합니다.
        });
    });

    // 모달 닫기
    closeButton.addEventListener("click", () => {
        modal.style.display = "none"; // 모달 닫기
    });

    window.addEventListener("click", (event) => {
        if (event.target === modal) {
            modal.style.display = "none"; // 모달 닫기
        }
    });

    // 더보기 버튼 클릭 이벤트
    moreButton.onclick = function() {
        if (additionalInfo.style.display === "none" || additionalInfo.style.display === "") {
            additionalInfo.style.display = "block"; // 추가 정보 표시
            this.textContent = "간략히"; // 버튼 텍스트 변경
        } else {
            additionalInfo.style.display = "none"; // 추가 정보 숨김
this.textContent = "더보기 ";

        }
    };
});
