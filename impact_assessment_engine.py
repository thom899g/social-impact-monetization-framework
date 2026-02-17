import logging
from dataclasses import dataclass
from typing import Optional, Dict, Any

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class SocialImpactMetrics:
    """Represents key social impact metrics used for assessment."""
    carbon_emissions_reduction: float
    education_reach: int
    community_engagement: float
    health_improvement: float
    economic_empowerment: float

class ImpactAssessmentEngine:
    """Evaluates the social impact of various initiatives and programs."""
    
    def __init__(self, metrics: SocialImpactMetrics):
        self.metrics = metrics
        self.impact_score_thresholds = {
            'high': 0.8,
            'medium': 0.5,
            'low': 0.2
        }
        
    def assess_impact(self) -> Dict[str, Any]:
        """Assesses the social impact based on provided metrics and returns a score."""
        try:
            # Calculate overall impact score
            total_score = (self.metrics.carbon_emissions_reduction * 
                         self.metrics.community_engagement * 
                         self.metrics.health_improvement)
            
            category_scores = {
                'environmental': self(metrics.carbon_emissions_reduction),
                'social': self(metrics.education_reach),
                'economic': self(metrics.economic_empowerment)
            }
            
            # Determine impact level
            if total_score >= self.impact_score_thresholds['high']:
                impact_level = 'high'
            elif total_score >= self.impact_score_thresholds['medium']:
                impact_level = 'medium'
            else:
                impact_level = 'low'
                
            logger.info(f"Impact assessment complete. Total score: {total_score}, Impact Level: {impact_level}")
            
            return {
                'total_impact_score': total_score,
                'category_scores': category_scores,
                'impact_level': impact_level
            }
            
        except Exception as e:
            logger.error(f"Error during impact assessment: {str(e)}")
            raise
        
    def __call__(self, value: float) -> float:
        """Helper method to normalize values between 0 and 1."""
        return (value - min(value)) / (max(value) - min(value))